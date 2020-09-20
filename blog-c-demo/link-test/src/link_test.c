#include <stdio.h>
#include "../head/hello.h"

/*
  三种方式输出可执行文件：
  1. 直接一次编译链接多个源文件： gcc *.c -o link_test && ./link_test
  2. 将hello.c制作为静态链接库（见hello.c文件注释说明），编译link_test.c时从静态库中链接：gcc link_test.c -o ../bin/static_link_test -L../lib -lhello_static
  3. 将hello.c制作为动态链接库（见hello.c文件注释说明），编译link_test.c时从动态库中链接：gcc link_test.c -o ../bin/dynamic_link_test -L../lib -lhello

  注意：
  1. 若lib目录下同时存在libhello.a或者libhello.so时，优先使用动态链接库so
  2. 动态链接时，执行文件的动态库搜索路径为相对路径，可用命令otool -L dynamic_link_test查看
     若切换到非编译时的目录执行文件，会报找不到动态库的错误，此时需要将动态库libhello.so移入/usr/local/lib下，重新编译gcc link_test.c -o ../bin/dynamic_link_test -lhello
     或者设置动态库的绝对路径install_name_tool -change ../lib/libhello.so ${absolute_path}
*/
int main(int argc, char const *argv[])
{
    // printf("hello, world\n");
    hello();
    return 123;
}
