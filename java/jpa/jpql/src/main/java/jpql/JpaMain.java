package jpql;

import javax.persistence.*;
import java.util.List;

public class JpaMain {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {

            Member member = new Member();
            member.setUsername("member1");
            member.setAge(20);
            em.persist(member);

            // 타입이 명확한 경우
            TypedQuery<Member> selectMFromMemberM = em.createQuery("select m from Member m", Member.class);
            TypedQuery<String> re1 = em.createQuery("select m.username from Member m", String.class);

            // 타입이 명확하지 않는 경우
            Query query = em.createQuery("select m.username, m.age from Member m");
            Query query1 = em.createQuery("select m from Member m");

            // 하나 확실할떄 없으면 에러남
            em.createQuery("select m from Member m", Member.class)
                    .getSingleResult();

            // 여러개 없으면 빈칸
            em.createQuery("select m from Member m", Member.class)
                    .getResultList();

            // 바인딩은 :parameter 혹은 ?1 문자
            em.createQuery("select m from Member m where m.username = :username", Member.class)
                            .setParameter("username", "member1")
                                    .getResultList();
            // 바인딩은 :parameter 혹은 ?1 문자
            em.createQuery("select m from Member m where m.username = ?1", Member.class)
                    .setParameter(1, "member1")
                    .getResultList();

            // object로
            List resultList = em.createQuery("select m.username, m.age from Member m")
                    .getResultList();
            for (Object o: resultList) {
                Object[] result = (Object[]) o;
                System.out.println("name: " + result[0]);
                System.out.println("age:" + result[1]);
            }

            // new 명령어로 조회

            // object로
            List<MemberDTO> resultList1 = em.createQuery("select new jpql.MemberDTO(m.username, m.age) from Member m", MemberDTO.class)
                    .getResultList();

            for (MemberDTO dto: resultList1) {
                System.out.println(dto.getUsername());
                System.out.println(dto.getAge());
            }

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
            System.out.println(e);
        } finally {
            em.close();
        }
        emf.close();
    }

}