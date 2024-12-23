package jpashop.jpabook.jpashop.domain2;

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
            User user = new User();
            user.setUsername("user1");

            User user2 = new User();
            user.setUsername("user2");

            em.persist(user);
            em.persist(user2);

            em.flush();
            em.clear();

//            User findUser = em.find(User.class, user.getId());

            User findUser = em.getReference(User.class, user.getId()); // 가짜객체를 가져와서
            System.out.println("class = " + findUser.getClass());
            System.out.println("id = " + findUser.getId()); // 해당 데이터가 필요한 시점에 sql에서 내요응ㄹ 가져옴,.
            System.out.println("name = " + findUser.getUsername());

            // 데이터타입 비교시 프록시 이므로 서로 안맞음.
            User u2 = em.find(User.class, user2.getId());
            System.out.println("비교: " + (findUser.getClass() == u2.getClass()));

            System.out.println("비교2: " + (findUser instanceof User)); // 따라서 객체 비교는 instanceof 를 써야함.
            // 만약 캐시된게 있으면 캐시된거를 그냥 가져다 쓴가 즉 원본객체를 쓴다.

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}
