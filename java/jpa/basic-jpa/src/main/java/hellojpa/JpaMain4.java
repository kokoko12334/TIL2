package hellojpa;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

public class JpaMain4 {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();

        try {
            tx.begin();
            Member member1 = new Member();
            member1.setUsername("ko");
            Member member2 = new Member();
            member2.setUsername("k1");
            Member member3 = new Member();
            member3.setUsername("k2");
//            member.setId(1L);
            System.out.println("##########");
            em.persist(member1);
            em.persist(member2);
            em.persist(member3);
            System.out.println("##########");

            tx.commit();

        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();

    }
}
