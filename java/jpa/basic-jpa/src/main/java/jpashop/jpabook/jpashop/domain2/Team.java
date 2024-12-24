package jpashop.jpabook.jpashop.domain2;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Team {

    @Id @GeneratedValue
    @Column(name = "id")
    private Long teamId;

    @Column(name = "name")
    private String teamName;

    @OneToMany(mappedBy = "team")
    private List<User> users = new ArrayList<>();

    public Team() {
    }

    public Long getTeamId() {
        return teamId;
    }

    public void setTeamId(Long teamId) {
        this.teamId = teamId;
    }

    public String getTeamName() {
        return teamName;
    }

    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    public List<User> getMembers() {
        return users;
    }

    public void setMembers(List<User> users) {
        this.users = users;
    }

}
