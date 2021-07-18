package cc.kejun.service.impl;

import cc.kejun.domain.PtUser;
import cc.kejun.dto.PageDTO;
import cc.kejun.dto.UserDTO;
import cc.kejun.mapper.PtUserMapper;
import cc.kejun.service.PtUserService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

/**
 * @author hch
 * @since 2021/7/17
 */
@Service
@RequiredArgsConstructor
public class PtUserServiceImpl implements PtUserService {
    private final PtUserMapper mapper;
    private final StringRedisTemplate stringRedisTemplate;
    private static final String COUNT_KEY = "pt:db:count";

    @Override
    public UserDTO getUser(Long id) {
        return new UserDTO(mapper.selectByPrimaryKey(id));
    }

    @Override
    public PageDTO<UserDTO> listUsers(Integer pageNum, Integer pageSize) {
        PageDTO<UserDTO> r = new PageDTO<>();
        // long count = mapper.count();
        long count = Long.parseLong(stringRedisTemplate.opsForValue().get(COUNT_KEY));

        r.setTotalCount(count);
        if (count < 1) {
            return r.setList(new ArrayList<>(0));
        }
        int totalPage = count / pageSize + count % pageSize == 0 ? 0 : 1;
        int pn = pageNum > totalPage ? totalPage : pageNum;
        r.setTotalPage(totalPage);
        r.setPageNum(pn);
        r.setPageSize(pageSize);
        List<PtUser> ptUsers = mapper.selectPage((pn - 1) * pageSize, pageSize);
        List<UserDTO> rList = new ArrayList<>(ptUsers.size());
        for (PtUser ptUser : ptUsers) {
            rList.add(new UserDTO(ptUser));
        }
        return r.setList(rList);
    }
}
