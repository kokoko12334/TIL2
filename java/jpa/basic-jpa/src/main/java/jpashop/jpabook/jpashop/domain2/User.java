package jpashop.jpabook.jpashop.domain2;

import javax.persistence.*;

@Entity
public class User {

    @Id @GeneratedValue
    @Column(name = "user_id")
    private Long id;

    @Column(name = "user_name")
    private String username;

    @ManyToOne
    @JoinColumn(name = "team2")
    private Team2 team2;

    public User() {
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

    public Team2 getTeam() {
        return team2;
    }

    public void setTeam(Team2 team2) {
        this.team2 = team2;
    }
}
