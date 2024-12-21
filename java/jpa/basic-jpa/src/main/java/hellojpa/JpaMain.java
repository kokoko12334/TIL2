package hellojpa;

import javax.persistence.*;
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

//            Member member1 = em.find(Member.class, 200L);
//            System.out.println(member1.getUsername());
//            System.out.println("#######################");
//
//            Member member2 = em.find(Member.class, 200L);
//            System.out.println(member2.getUsername());
//            System.out.println("#######################");
//
//            em.detach(member1);
//            Member member3 = em.find(Member.class, 200L);
//            System.out.println(member3.getUsername());
//            System.out.println("#######################");

            Team team = new Team();
            team.setTeamName("team2");
            em.persist(team);

            Member member = new Member();
            member.setUsername("koko2");
            member.setTeam(team);

            Member member2 = new Member();
            member2.setUsername("koko2112");
            member2.setTeam(team);

            em.persist(member);
            em.persist(member2);

            // 캐시 무효화
            em.flush();
            em.clear();

            Member findMember = em.find(Member.class, member.getId());
            Team findTeam = findMember.getTeam();

            List<Member> members = findTeam.getMembers();

            for (Member m: members) {
                System.out.println(m.getUsername());
            }

            System.out.println("team:=" + findTeam.getTeamName());

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
