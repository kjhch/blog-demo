#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#define PORT 8888

int main(int argc, char const *argv[])
{
    int sock, new_sock;
    struct sockaddr_in my_addr, client_addr;
    int len;
    char buf[100];
    char buf2[128];
    int recdata = 0;
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("socket create error\n");
        exit(1);
    }

    memset(&my_addr, 0, sizeof(my_addr));
    my_addr.sin_family = AF_INET;
    my_addr.sin_port = htons(PORT);
    my_addr.sin_addr.s_addr = INADDR_ANY;
    if (bind(sock, (struct sockaddr *)&my_addr, sizeof(my_addr)) == -1)
    {
        perror("bind error");
        exit(1);
    }

    if (listen(sock, 5) < 0)
    {
        perror("listen error\n");
        exit(1);
    }
    printf("listen at %s:%d\n", my_addr.sin_addr.s_addr, PORT);

    while (1)
    {
        len = sizeof(struct sockaddr);
        if ((new_sock = accept(sock, (struct sockaddr *)&client_addr, &len)) < 0)
        {
            perror("accept error\n");
            exit(1);
        }
        else
        {
            printf("server: get connection from %s, port %d, socket %d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port), new_sock);
        }

        while (1)
        {

            len = recv(new_sock, buf, 100, 0);
            if (len < 0)
            {
                printf("recv error\n");
                exit(1);
            }
            else if (len == 0)
            {
                printf("client quit\n");
                break;
            }
            else
            {
                buf[len] = '\0';
                printf("receive message: %s\n", buf);
                recdata = atoi(buf);
                recdata++;
                sprintf(buf2, "%d", recdata);
                if (send(new_sock, buf2, strlen(buf2), 0) < 0)
                {
                    perror("send data failed\n");
                }
            }
        }
        close(new_sock);
    }
    close(sock);
    return 0;
}
