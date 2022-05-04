import os
os.system('pip install sentencepiece')

# Seq2Seq-Attention Machine Translator : 학습 데이터 모듈
# Google의 Sentencepiece를 이용해서 학습 데이터를 생성한다.
#
# 저작자: 2021.08.02, 조성현 (blog.naver.com/chunjein)
# copyright: SNS 등에 공개할 때는 출처에 저작자를 명시해 주시기 바랍니다.
# -------------------------------------------------------------------
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import pandas as pd
import sentencepiece as spm
import re
import pickle
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# 작업 디렉토리를 변경한다.
# %cd '/content/drive/My Drive/Colab Notebooks'

# 데이터 파일을 읽어온다.
path = "C:/Users/user/Desktop/file/"
df = pd.read_csv(path + 'machine_trans.csv', header=0)
source, target = list(df['source']), list(df['target'])
df.head()

# 학습 데이터와 시험 데이터를 분리한다.
src_train, src_test, tar_train, tar_test = train_test_split(source, target, test_size=0.1, random_state=0)

src_train[0], tar_train[0]

# Google의 Sentencepiece를 이용해서 vocabulary를 생성한다.
# -----------------------------------------------------
templates= "--input={} \
            --pad_id=0 --pad_piece=<PAD>\
            --unk_id=1 --unk_piece=<UNK>\
            --bos_id=2 --bos_piece=<BOS>\
            --eos_id=3 --eos_piece=<EOS>\
            --model_prefix={} \
            --vocab_size={}"

# Sentencepice용 한글 (source) 사전을 만들기 위해 src_train + src_test를 저장해 둔다.
data_file = path + "mt_source.txt"
with open(data_file, 'w', encoding='utf-8') as f:
    for sent in src_train + src_test:
        f.write(sent + '\n')

SRC_VOCAB = 9000
model_prefix = path + "source_model"
params = templates.format(data_file, model_prefix, SRC_VOCAB)

spm.SentencePieceTrainer.Train(params)
sp_source = spm.SentencePieceProcessor()
sp_source.Load(model_prefix + '.model')

with open(model_prefix + '.vocab', encoding='utf-8') as f:
    vocab = [doc.strip().split('\t') for doc in f]

src_word2idx = {k:v for v, [k, _] in enumerate(vocab)}
src_idx2word = {v:k for v, [k, _] in enumerate(vocab)}

print([src_idx2word[i] for i in range(20)])

# Sentencepice용 영어 (target) 사전을 만들기 위해 tar_train + tar_test를 저장해 둔다.
data_file = path + "mt_target.txt"
with open(data_file, 'w', encoding='utf-8') as f:
    for sent in tar_train + tar_test:
        f.write(sent + '\n')

TAR_VOCAB = 4798
model_prefix = path + "target_model"
params = templates.format(data_file, model_prefix, TAR_VOCAB)

spm.SentencePieceTrainer.Train(params)
sp_target = spm.SentencePieceProcessor()
sp_target.Load(model_prefix + '.model')

with open(model_prefix + '.vocab', encoding='utf-8') as f:
    vocab = [doc.strip().split('\t') for doc in f]

tar_word2idx = {k:v for v, [k, _] in enumerate(vocab)}
tar_idx2word = {v:k for v, [k, _] in enumerate(vocab)}

print([tar_idx2word[i] for i in range(20)])

# 학습 데이터를 생성한다. (인코더 입력용, 디코더 입력용, 디코더 출력용)
MAX_LEN_SRC = 15
MAX_LEN_TAR = 20
enc_input = []
dec_input = []
dec_output = []

for src, tar in zip(src_train, tar_train):
    # Encoder 입력
    enc_i = sp_source.encode_as_ids(src)
    enc_input.append(enc_i)

    # Decoder 입력, 출력
    dec_i = [sp_target.bos_id()]   # <BOS>에서 시작함
    dec_o = []
    for ans in sp_target.encode_as_ids(tar):
        dec_i.append(ans)
        dec_o.append(ans)
    dec_o.append(sp_target.eos_id())   # Encoder 출력은 <EOS>로 끝남.        
    
    # dec_o는 <EOS>가 마지막에 들어있다. 나중에 pad_sequences()에서 <EOS>가
    # 잘려 나가지 않도록 MAX_LEN 위치에 <EOS>를 넣어준다.
    if len(dec_o) > MAX_LEN_TAR:
        dec_o[MAX_LEN_TAR] = sp_target.eos_id()
        
    dec_input.append(dec_i)
    dec_output.append(dec_o)

# 문장 길이 분포를 파악한다.
sns.displot([len(s) for s in dec_input])

# 각 문장의 길이를 맞추고 남는 부분에 padding을 삽입한다.
enc_input = pad_sequences(enc_input, maxlen=MAX_LEN_SRC, value = sp_source.pad_id(), padding='post', truncating='post')
dec_input = pad_sequences(dec_input, maxlen=MAX_LEN_TAR, value = sp_target.pad_id(), padding='post', truncating='post')
dec_output = pad_sequences(dec_output, maxlen=MAX_LEN_TAR, value = sp_target.pad_id(), padding='post', truncating='post')

# 사전과 학습 데이터를 저장한다.
with open(path + 'mt_voc.pkl', 'wb') as f:
    pickle.dump([src_word2idx, src_idx2word, tar_word2idx, tar_idx2word], f, pickle.HIGHEST_PROTOCOL)

# BLEU 평가를 위해 que_test와 ans_test를 저장해 둔다.
with open(path + 'mt_train.pkl', 'wb') as f:
    pickle.dump([enc_input, dec_input, dec_output, src_test, tar_test], f, pickle.HIGHEST_PROTOCOL)

enc_input[0]

dec_input[0]

dec_output[0]

[(s, t) for s, t in zip(src_train[:10], tar_train[:10])]

[(s, t) for s, t in zip(src_test[:10], tar_test[:10])]


###################

22222

#####

# Commented out IPython magic to ensure Python compatibility.
# 작업 디렉토리를 변경한다.
# %cd '/content/drive/My Drive/Colab Notebooks'

# Seq2Seq-Attention 모델를 이용한 Machine Translator : 기계번역 수행 모듈
#
# 저작자: 2021.08.02, 조성현 (blog.naver.com/chunjein)
# copyright: SNS 등에 공개할 때는 출처에 저작자를 명시해 주시기 바랍니다.
# ----------------------------------------------------------------------
from tensorflow.keras.layers import Input, LSTM, Dense, Dot, Concatenate
from tensorflow.keras.layers import Embedding, TimeDistributed, Activation
from tensorflow.keras.models import Model
import tensorflow.keras.backend as K
import sentencepiece as spm
import numpy as np
import pickle
from tqdm.auto import tqdm

# 서브워드 사전을 읽어온다.
with open(path + 'mt_voc.pkl', 'rb') as f:
    src_word2idx,  src_idx2word, tar_word2idx, tar_idx2word = pickle.load(f)

# 시험 데이터를 읽어온다.
with open(path + 'mt_train.pkl', 'rb') as f:
    _, _, _, src_test, tar_test = pickle.load(f)

SRC_VOCAB = len(src_idx2word)
TAR_VOCAB = len(tar_idx2word)
EMB_SIZE = 128
LSTM_HIDDEN = 128
MAX_LEN_SRC = 15
MAX_LEN_TAR = 20
MODEL_PATH = path + 'mt_attention.h5'
# LOAD_MODEL = False


# 데이터 전처리 과정에서 생성한 SentencePiece model을 불러온다.
sp_source = spm.SentencePieceProcessor()
sp_target = spm.SentencePieceProcessor()
sp_source.Load(path + "source_model.model")
sp_target.Load(path + "target_model.model")

# Seq2Seq-Attention 모델을 생성한다.
K.clear_session()

# Encoder
# -------
encoderX = Input(batch_shape=(None, MAX_LEN_SRC))
encEMB = Embedding(input_dim=SRC_VOCAB, output_dim=EMB_SIZE)(encoderX)
encLSTM1 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
encLSTM2 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
ey1, eh1, ec1 = encLSTM1(encEMB)      # LSTM 1층 
ey2, eh2, ec2 = encLSTM2(ey1)         # LSTM 2층

# Decoder
# -------
# Decoder는 1개 단어씩을 입력으로 받는다. 학습 때와 달리 문장 전체를 받아
# recurrent하는 것이 아니라, 단어 1개씩 입력 받아서 다음 예상 단어를 확인한다.
# chatting()에서 for 문으로 단어 별로 recurrent 시킨다.
# 따라서 batch_shape = (None, 1)이다. 즉, time_step = 1이다. 그래도 네트워크
# 파라메터는 동일하다.
decoderX = Input(batch_shape=(None, 1))
decEMB = Embedding(input_dim=TAR_VOCAB, output_dim=EMB_SIZE)(decoderX)
decLSTM1 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state=True)
decLSTM2 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state=True)
dy1, _, _ = decLSTM1(decEMB, initial_state = [eh1, ec1])
dy2, _, _ = decLSTM2(dy1, initial_state = [eh2, ec2])
decOutput = TimeDistributed(Dense(TAR_VOCAB, activation='softmax'))
outputY = decOutput(dy2)

# Model
# -----
model = Model([encoderX, decoderX], outputY)
model.load_weights(MODEL_PATH)

# 기계번역 model
model_enc = Model(encoderX, [eh1, ec1, eh2, ec2, ey2])

ih1 = Input(batch_shape = (None, LSTM_HIDDEN))
ic1 = Input(batch_shape = (None, LSTM_HIDDEN))
ih2 = Input(batch_shape = (None, LSTM_HIDDEN))
ic2 = Input(batch_shape = (None, LSTM_HIDDEN))
ey = Input(batch_shape = (None, MAX_LEN_SRC, LSTM_HIDDEN))

dec_output1, dh1, dc1 = decLSTM1(decEMB, initial_state = [ih1, ic1])
dec_output2, dh2, dc2 = decLSTM2(dec_output1, initial_state = [ih2, ic2])
dec_output = decOutput(dec_output2)
model_dec = Model([decoderX, ih1, ic1, ih2, ic2, ey], 
                  [dec_output, dh1, dc1, dh2, dc2])

# Source 문장을 입력받아 target문장을 생성한다.
def genAnswer(source):
    source = source[np.newaxis, :]
    init_h1, init_c1, init_h2, init_c2, enc_y = model_enc.predict(source)

    # 시작 단어는 <BOS>로 한다.
    word = np.array(sp_target.bos_id()).reshape(1, 1)

    target = []
    for i in range(MAX_LEN_TAR):
        dY, next_h1, next_c1, next_h2, next_c2 = \
            model_dec.predict([word, init_h1, init_c1, init_h2, init_c2, enc_y])
        
        # 디코더의 출력은 vocabulary에 대응되는 one-hot이다.
        # argmax로 해당 단어를 채택한다.
        nextWord = np.argmax(dY[0, 0])

        # 예상 단어가 <EOS>이거나 <PAD>이면 더 이상 예상할 게 없다.
        if nextWord == sp_target.eos_id() or nextWord == sp_target.pad_id():
            break
        
        # 다음 예상 단어인 디코더의 출력을 target에 추가한다.
        target.append(tar_idx2word[nextWord])
        
        # 디코더의 다음 recurrent를 위해 입력 데이터와 hidden 값을
        # 준비한다. 입력은 word이고, hidden은 h와 c이다.
        word = np.array(nextWord).reshape(1,1)
    
        init_h1 = next_h1
        init_c1 = next_c1
        init_h2 = next_h2
        init_c2 = next_c2
        
    return sp_target.decode_pieces(target)

def make_question(src_string):
    src_idx = []
    for x in sp_source.encode_as_pieces(src_string):
        if x in src_word2idx:
            src_idx.append(src_word2idx[x])
        else:
            src_idx.append(sp_source.unk_id())   # out-of-vocabulary (OOV)
    
    # <PAD>를 삽입한다.
    if len(src_idx) < MAX_LEN_SRC:
        src_idx.extend([sp_source.pad_id()] * (MAX_LEN_SRC - len(src_idx)))
    else:
        src_idx = src_idx[0:MAX_LEN_SRC]
    return src_idx

# 기계번역 수행.
# dummy : 최초 1회는 모델을 로드하는데 약간의 시간이 걸리므로 이것을 가리기 위함.
def translate(n=100):
    for i in range(n):
        source = input('Source : ')
        
        if  source == 'quit':
            break
        
        src_idx = make_question(source)
        target = genAnswer(np.array(src_idx))
        print('Target :', target)

####### 기계번역 시작 #######
print("\nSeq2Seq-Attention Machine Translator (ver. 1.0)")
print("기계번역 모듈을 로드하고 있습니다 ...")

# 처음 1회는 시간이 걸리기 때문에 dummy source를 입력한다.
target = genAnswer(np.zeros(MAX_LEN_SRC))
print("기계번역 모듈이 준비 됐습니다.\n")

# 번역을 시작한다.
translate(100)

# train data:
# [('요리하는게 재밌어', "It's fun to cook"),
#  ('첫만남 그리고 끝', 'First meeting and end'),
#  ('볼 수가 없군요', 'I can not see it.'),
#  ('이상형은 아니지만 호감가는 사람이 있어요', "I'm not an ideal, but I have a crush."),
#  ('이별 준비 중', 'Preparing for separation'),
#  ('자꾸 생각하면 더 힘들어요', "It's harder to keep thinking."),
#  ('내 집 마련 축하드려요', 'I am celebrating my house.'),
#  ('헤어진지 43일', '43 days'),
#  ('마음이 시키는데로 하면 되요', 'I want you to make it.'),
#  ('사정이 뭔지 모르겠지만 좋아하는 건 괜찮아요',
#   "I do not know what the situation is, but I like it's okay.")]

# test data:
# [('눈을 크게 뜨고 잘 찾아보세요', 'Find your eyes and find it well.'),
#  ('나쁜 사람일지도 모르겠네요', 'I do not know a bad person.'),
#  ('거창하지 않아도 돼요', 'I do not have to be a tremend.'),
#  ('썸 타다 지쳤어', "I'm tired of it."),
#  ('사랑의 힘인가봐요', "I think it's the power of love."),
#  ('변하는 건 사랑이겠죠', "It's love to change."),
#  ('이제 짝사랑 말고 둘이서 하는 사랑하세요', 'I love you two,'),
#  ('짝남한테 계속 친한 척하면 부담스러워 할까',
#   'If you keep pretending to be close to the mild man, will it be burdensome?'),
#  ('어른이 된다는 것', 'Manger'),
#  ('꼭 사랑한다고 말해야 사랑하는건 아니라고 생각해요', 'I think I do not love you to say that I love you.')]

src_test[0], tar_test[0]

n = 50
y_test = tar_test[:n]

y_pred = []
for src in tqdm(y_test, total=len(y_test)):
    src_idx = make_question(src)
    src_ans = genAnswer(np.array(src_idx))
    y_pred.append(src_ans)

from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

y_test1 = [[x.split()] for x in y_test]
y_pred1 = [x.split() for x in y_pred]

bleu_score = corpus_bleu(y_test1, y_pred1, weights=(1,0,0,0), smoothing_function=SmoothingFunction().method1)
print('BLEU score =', bleu_score)


###############
333
################




# Seq2Seq-Attention 모델를 이용한 Machine Translator : 학습 모듈
#
# 관련 논문 : Kyunghyun Cho, et. al., 2014,
#             Learning Phrase Representations using RNN Encoder–Decoder 
#             for Statistical Machine Translation
#
# 코드 구현 : 2021.08.02, 조성현 (blog.naver.com/chunjein)
# copyright: SNS 등에 공개할 때는 출처에 저작자를 명시해 주시기 바랍니다.
# ----------------------------------------------------------------------
from tensorflow.keras.layers import Input, LSTM, Dense, Dot, Concatenate
from tensorflow.keras.layers import Embedding, TimeDistributed, Activation
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
import tensorflow.keras.backend as K
import matplotlib.pyplot as plt
import pickle
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# Commented out IPython magic to ensure Python compatibility.
# 작업 디렉토리를 변경한다.
# %cd '/content/drive/My Drive/Colab Notebooks'

# 서브워드 사전을 읽어온다.
with open(path + 'mt_voc.pkl', 'rb') as f:
    src_word2idx,  src_idx2word, tar_word2idx, tar_idx2word = pickle.load(f)
    
# 학습 데이터 : 인코딩, 디코딩 입력, 디코딩 출력을 읽어온다.
with open(path + 'mt_train.pkl', 'rb') as f:
    trainXE, trainXD, trainYD, _, _ = pickle.load(f)

SRC_VOCAB = len(src_idx2word)
TAR_VOCAB = len(tar_idx2word)
EMB_SIZE = 128
LSTM_HIDDEN = 128
MODEL_PATH = path + 'mt_attention.h5'
LOAD_MODEL = False

# Seq2Seq-Attention 모델을 생성한다.
K.clear_session()

# Encoder
# -------
# many-to-many로 구성한다. Attention value를 계산하기 위해 중간 출력이 필요하고
# (return_sequences=True), decoder로 전달할 h와 c도 필요하다 (return_state = True)
encoderX = Input(batch_shape=(None, trainXE.shape[1]))
encEMB = Embedding(input_dim=SRC_VOCAB, output_dim=EMB_SIZE)(encoderX)
encLSTM1 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
encLSTM2 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state = True)
ey1, eh1, ec1 = encLSTM1(encEMB)    # LSTM 1층 
ey2, eh2, ec2 = encLSTM2(ey1)       # LSTM 2층

# Decoder
# -------
# many-to-many로 구성한다. target을 학습하기 위해서는 중간 출력이 필요하다.
# 그리고 초기 h와 c는 encoder에서 출력한 값을 사용한다 (initial_state)
# 최종 출력은 vocabulary의 인덱스인 one-hot 인코더이다.
decoderX = Input(batch_shape=(None, trainXD.shape[1]))
decEMB = Embedding(input_dim=TAR_VOCAB, output_dim=EMB_SIZE)(decoderX)
decLSTM1 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state=True)
decLSTM2 = LSTM(LSTM_HIDDEN, return_sequences=True, return_state=True)
dy1, _, _ = decLSTM1(decEMB, initial_state = [eh1, ec1])
dy2, _, _ = decLSTM2(dy1, initial_state = [eh2, ec2])
decOutput = TimeDistributed(Dense(TAR_VOCAB, activation='softmax'))
outputY = decOutput(dy2)

# Model
# -----
model = Model([encoderX, decoderX], outputY)
model.compile(optimizer=optimizers.Adam(learning_rate=0.0005), loss='sparse_categorical_crossentropy')

if LOAD_MODEL:
    model.load_weights(MODEL_PATH)
model.summary()


# 학습 (teacher forcing)
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
hist = model.fit([trainXE, trainXD], trainYD, batch_size = 512, epochs=100, shuffle=True)

# 학습 결과를 저장한다
model.save_weights(MODEL_PATH)

# Loss history를 그린다
plt.plot(hist.history['loss'], label='Train loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()







