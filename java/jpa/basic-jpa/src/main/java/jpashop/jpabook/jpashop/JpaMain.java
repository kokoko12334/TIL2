package jpashop.jpabook.jpashop;

import jpashop.jpabook.jpashop.domain.Member;
import jpashop.jpabook.jpashop.domain.embedded.Address;
import jpashop.jpabook.jpashop.domain.embedded.Period;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.time.LocalDateTime;
import java.util.List;

public class JpaMain {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {

            Member member = new Member();
            member.setName("koko");
            member.setAddress(new Address("city", "add", "zip132"));
            member.setWorkPeriod(new Period(LocalDateTime.now(), LocalDateTime.now()));
            em.persist(member);

            List<Member> members = em.createQuery("select m from Member m where m.name like '%k%'", Member.class).getResultList();

            for (Member member1: members) {
                System.out.println(member1);
            }

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}

