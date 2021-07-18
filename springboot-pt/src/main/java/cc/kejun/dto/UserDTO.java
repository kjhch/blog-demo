package cc.kejun.dto;

import cc.kejun.domain.PtUser;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;

import java.io.Serializable;

/**
 * @author hch
 * @since 2021/7/17
 */
@Data
@JsonInclude(JsonInclude.Include.NON_NULL)
public class UserDTO implements Serializable {
    private static final long serialVersionUID = -1248185897923805901L;
    private Long id;

    /**
     *
     */
    private String username;

    /**
     *
     */
    private String gender;

    /**
     *
     */
    private String phone;

    /**
     *
     */
    private String email;

    /**
     *
     */
    private String address;


    public UserDTO(PtUser ptUser) {
        this.id = ptUser.getId();
        this.username = ptUser.getUsername();
        this.gender = String.valueOf(ptUser.getGender());
        this.phone = ptUser.getPhone();
        this.email = ptUser.getEmail();
        this.address = ptUser.getAddress();
    }
}
