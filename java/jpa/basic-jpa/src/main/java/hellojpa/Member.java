package hellojpa;

import javax.persistence.*;
import java.util.Date;

@Entity
//@Table(name = "mbf")
//@SequenceGenerator(
//        name = "seq_generator",
//        sequenceName = "ko_seq", // 시퀀스 객체 이름
//        initialValue = 1, allocationSize = 50
//)
public class Member {

//    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "seq_generator")
    @Id @GeneratedValue
    private Long id;

    @Column(name = "name")
    private String username;

    @ManyToOne //자기가 many
    @JoinColumn(name = "TEAM_ID")
    private Team team;

    public Member() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Team getTeam() {
        return team;
    }

    public void setTeam(Team team) {

        this.team = team;
        team.getMembers().add(this);
    }

    @Override
    public String toString() {
        return "Member{" +
                "team=" + team +
                ", username='" + username + '\'' +
                ", id=" + id +
                '}';
    }
}
