package jpashop.jpabook.jpashop.domain2;

import org.hibernate.Hibernate;
import org.hibernate.annotations.Proxy;
import org.hibernate.engine.spi.PersistenceContext;
import org.hibernate.engine.spi.SessionImplementor;

import javax.persistence.*;

public class JpaMain {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();

        tx.begin();
        try {
            Team team = new Team();
            team.setTeamName("team2");
            em.persist(team);


            User user = new User();
            user.setUsername("kokoko");
            user.setTeam(team);
            em.persist(user);
//
//            User user2 = new User();
//            user2.setUsername("user2");
//
//            em.persist(user);
//            em.persist(user2);

            em.flush();
            em.clear();

            System.out.println("#####find user####");
            User findUser = em.find(User.class, user.getId());

            System.out.println("### team에 대한 정보를 불러올 때");
            findUser.getTeam().getTeamName();

//            System.out.println("member: " + findUser.getClass());
//            Team team2 = findUser.getTeam();
//            System.out.println("team: " + team2.getClass());

//            team2.getTeamName();
//            System.out.println(team2.getClass());

//            User findUser = em.getReference(User.class, user.getId()); // 가짜객체를 가져와서
            System.out.println("findUser의 class = " + findUser.getClass());

//            Hibernate.initialize(findUser);
//            findUser.getId();
            System.out.println("초기화 이후 finUser의 class = " + findUser.getClass());
            SessionImplementor session2 = em.unwrap(SessionImplementor.class);
            PersistenceContext persistenceContext2 = session2.getPersistenceContext();
            System.out.println("###############");
            persistenceContext2.getEntitiesByKey().forEach((key, value) -> {
                System.out.println("Entity: " + key + " -> " + value);
            });


//            // 데이터타입 비교시 프록시 이므로 서로 안맞음.
//            User u2 = em.find(User.class, user2.getId());
//            System.out.println("비교: " + (findUser.getClass() == u2.getClass()));
//
//            System.out.println("비교2: " + (findUser instanceof User)); // 따라서 객체 비교는 instanceof 를 써야함.
//            // 만약 캐시된게 있으면 캐시된거를 그냥 가져다 쓴가 즉 원본객체를 쓴다.

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}
