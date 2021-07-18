package cc.kejun.service;

import cc.kejun.dto.PageDTO;
import cc.kejun.dto.UserDTO;

/**
 * @author hch
 * @since 2021/7/17
 */
public interface PtUserService {
    UserDTO getUser(Long id);

    PageDTO<UserDTO> listUsers(Integer pageNum, Integer pageSize);
}
