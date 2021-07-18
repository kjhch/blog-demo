package cc.kejun.controller;

import cc.kejun.dto.PageDTO;
import cc.kejun.dto.ResponseDTO;
import cc.kejun.dto.UserDTO;
import cc.kejun.service.PtUserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author hch
 * @since 2021/7/17
 */
@RestController
@RequiredArgsConstructor
public class PtController {
    private final PtUserService service;

    @GetMapping("/")
    public String index() {
        return "springboot-pt";
    }

    @GetMapping("/user")
    public ResponseDTO<UserDTO> user(@RequestParam("id") Long id) {
        return new ResponseDTO<>(service.getUser(id));
    }

    @GetMapping("/users")
    public ResponseDTO<PageDTO<UserDTO>> users(@RequestParam("pageNum") Integer pageNum,
                                               @RequestParam("pageSize") Integer pageSize) {
        return new ResponseDTO<>(service.listUsers(pageNum, pageSize));
    }

}
