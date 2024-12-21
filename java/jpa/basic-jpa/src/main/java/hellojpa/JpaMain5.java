package hellojpa;


import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.util.List;

public class JpaMain5 {

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

            Member member2 = new Member();
            member2.setUsername("user1");
            member2.setTeam(team1);
            em.persist(member2);

            Member member3 = new Member();
            member3.setUsername("user1");
            member3.setTeam(team1);
            em.persist(member3);

            em.flush();
            em.clear();

            Member findMember = em.find(Member.class, member1.getId());
            Team team = findMember.getTeam();
            List<Member> members = team.getMembers();

            for (Member member: members) {
                System.out.println(member);
            }

            tx.commit();
        } catch(Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }

}
