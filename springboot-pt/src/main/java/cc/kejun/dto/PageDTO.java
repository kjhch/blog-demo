package cc.kejun.dto;

import lombok.Data;
import lombok.experimental.Accessors;

import java.io.Serializable;
import java.util.List;

/**
 * @author hch
 * @since 2021/7/17
 */
@Data
@Accessors(chain = true)
public class PageDTO<T> implements Serializable {
    private static final long serialVersionUID = 5401446163338925747L;
    private Integer pageNum;
    private Integer pageSize;
    private Integer totalPage;
    private Long totalCount;
    private List<T> list;
}
