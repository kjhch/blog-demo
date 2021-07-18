package cc.kejun.mapper;

import cc.kejun.domain.PtUser;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface PtUserMapper {

    int deleteByPrimaryKey(Long id);

    int insert(PtUser record);

    int insertSelective(PtUser record);

    PtUser selectByPrimaryKey(Long id);

    int updateByPrimaryKeySelective(PtUser record);

    int updateByPrimaryKey(PtUser record);

    long count();

    List<PtUser> selectPage(@Param("offset") Integer offset, @Param("limit") Integer limit);
}
