package jpashop.jpabook.jpashop;

import jpashop.jpabook.jpashop.domain.Locker;
import jpashop.jpabook.jpashop.domain.Member;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

public class JpaMain {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
            Locker locker = new Locker();
            locker.setName("locker1");
            em.persist(locker);

            Member member = new Member();
            member.setCity("seoul");
            member.setName("ko");
            member.setStreet("sinki");
            member.setZipcode("dsdsd");
            member.setLocker(locker);
            em.persist(member);

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}

