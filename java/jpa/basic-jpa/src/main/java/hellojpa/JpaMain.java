package hellojpa;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.util.List;

public class JpaMain {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {

//            List<Member> result = em.createQuery("select m from Member as m", Member.class)
//                    .getResultList();
//
//            for (Member member: result) {
//                System.out.println("memberName = " + member.getName());
//            }

//            Member member = em.find(Member.class, 3L);
//            member.setName("Hel1"); // 변경등 수정사항은 트랜잭션이 알아서 persist함
//            em.persist(member); // 저장

//            long start = System.currentTimeMillis();
//            for (long i=1L; i <= 10000L; i++) {
////                tx.begin();
//                Member member = new Member();
//                member.setId(i);
//                member.setName("name" + i);
//                em.persist(member);
////                tx.commit();
//            }

            Member member1 = em.find(Member.class, 200L);
            System.out.println(member1.getUsername());
            System.out.println("#######################");

            Member member2 = em.find(Member.class, 200L);
            System.out.println(member2.getUsername());
            System.out.println("#######################");

            em.detach(member1);
            Member member3 = em.find(Member.class, 200L);
            System.out.println(member3.getUsername());
            System.out.println("#######################");
            tx.commit();
//            long end = System.currentTimeMillis();

//            System.out.println("걸린시간(초): " + (end - start));
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}
