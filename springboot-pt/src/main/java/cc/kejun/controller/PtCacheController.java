package cc.kejun.controller;

import cc.kejun.dto.PageDTO;
import cc.kejun.dto.ResponseDTO;
import cc.kejun.dto.UserDTO;
import cc.kejun.service.PtUserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author hch
 * @since 2021/7/18
 */
@RestController
@RequestMapping("/cache")
@RequiredArgsConstructor
@Slf4j
public class PtCacheController {
    private final PtUserService service;
    private static final String REDIS_KEY_PREFIX = "pt";

    @GetMapping("/user")
    @Cacheable(value = REDIS_KEY_PREFIX, key = "'user:'+#id", unless = "#result==null")
    public ResponseDTO<UserDTO> user(@RequestParam("id") Long id) {
        log.debug("no cache");
        return new ResponseDTO<>(service.getUser(id));
    }

    @GetMapping("/users")
    @Cacheable(value = REDIS_KEY_PREFIX, key = "'users:'+#pageNum+'-'+#pageSize", unless = "#result==null")
    public ResponseDTO<PageDTO<UserDTO>> users(@RequestParam("pageNum") Integer pageNum,
                                               @RequestParam("pageSize") Integer pageSize) {
        return new ResponseDTO<>(service.listUsers(pageNum, pageSize));
    }
}
