package jpashop.jpabook.jpashop.domain2;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.util.List;

public class JpaNplusMain {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();

        tx.begin();
        try {

            Team team1 = new Team();
            team1.setTeamName("team1");
            em.persist(team1);

            Team team2 = new Team();
            team2.setTeamName("team2");
            em.persist(team2);

            User user1 = new User();
            user1.setUsername("user1");
            user1.setTeam(team1);
            em.persist(user1);

            User user2 = new User();
            user2.setUsername("user2");
            user2.setTeam(team2);
            em.persist(user2);

            em.flush();
            em.clear();
//
//            List<User> users = em.createQuery("select u from User u", User.class)
//                                .getResultList();

            //fetchjoin
            List<User> users = em.createQuery("select u from User u join fetch u.team", User.class)
                    .getResultList();

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}
