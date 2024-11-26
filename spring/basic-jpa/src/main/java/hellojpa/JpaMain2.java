package hellojpa;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

public class JpaMain2 {
    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();
        tx.begin();
        try {

            Member findMember = em.find(Member.class, 500L);
            System.out.println("id=" + findMember.getId());
            System.out.println("name=" + findMember.getName());

            System.out.println("Second request"); // 영속성 컨테스트에 저장되기 때문에 1차캐시에서 조회함 그래서 쿼리문이 안나감.
            Member findMember2 = em.find(Member.class, 500L);
            System.out.println("id=" + findMember2.getId());
            System.out.println("name=" + findMember2.getName());

            System.out.println(findMember == findMember2);

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}

