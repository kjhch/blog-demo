package cc.kejun;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

import java.util.Optional;

/**
 * @author hch
 * @since 2021/7/17
 */
@SpringBootApplication
@Slf4j
@EnableCaching
public class Application {
    public static final String SPRING_PROFILES_ACTIVE = "spring.profiles.active";
    public static final String SPRING_PROFILES_ACTIVE_ENV = "SPRING_PROFILES_ACTIVE";

    public static void main(String[] args) {
        setupDefaultProfile(args);
        SpringApplication.run(Application.class, args);
    }

    private static void setupDefaultProfile(String[] args) {
        String vmOptProfile = System.getProperty(SPRING_PROFILES_ACTIVE);
        String sysEnvProfile = Optional.ofNullable(System.getenv(SPRING_PROFILES_ACTIVE))
                .orElse(System.getenv(SPRING_PROFILES_ACTIVE_ENV));
        String cmdProfile = null;
        for (String arg : args) {
            if (arg.contains(SPRING_PROFILES_ACTIVE)) {
                cmdProfile = arg;
                break;
            }
        }
        boolean noVmOptProfile = vmOptProfile == null;
        boolean noSysEnvProfile = sysEnvProfile == null;
        boolean noCmdProfile = cmdProfile == null;
        log.debug("vmOptProfile: {}, sysEnvProfile: {}, cmdProfile: {}", vmOptProfile, sysEnvProfile, cmdProfile);

        // 未通过虚拟机参数、系统环境变量以及命令行指定profile，则使用dev
        if (noVmOptProfile && noSysEnvProfile && noCmdProfile) {
            System.setProperty(SPRING_PROFILES_ACTIVE, "dev");
        }
    }
}
