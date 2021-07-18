package cc.kejun.dto;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

/**
 * @author hch
 * @since 2021/7/17
 */
@Data
@NoArgsConstructor
public class ResponseDTO<T> implements Serializable {
    private static final long serialVersionUID = 8085799105961113184L;
    private String code;
    private String message;
    private T data;

    public ResponseDTO(T data) {
        this.code = "00000";
        this.message = "success";
        this.data = data;
    }
}
