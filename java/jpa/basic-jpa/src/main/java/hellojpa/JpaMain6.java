package hellojpa;


import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.util.List;

public class JpaMain6 {

    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();
        try {
            Team team1 = new Team();
            team1.setTeamName("team1");
            em.persist(team1);

            Member member1 = new Member();
            member1.setUsername("user1");
            member1.setTeam(team1);
            em.persist(member1);

//            team1.getMembers().add(member1); // 양쪽에다 해야 캐쉬된거에서도 반영이 즉 컨ㄴ텍스트에서 반영이 된다.

//            em.flush();
//            em.clear();

            Member findMember = em.find(Member.class, member1.getId()); // 영속성 컨텍스트에서 없으면 순수한 객체를 불러오기 때문에 에러
            // 따라서 양쪽에 add 하는 것도 필요
            Team team = findMember.getTeam();
            List<Member> members = team.getMembers();

//            System.out.println("############");
//            for (Member member: members) {
//                System.out.println(member);
//            }
//            System.out.println("############");

            tx.commit();
        } catch(Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }

}
