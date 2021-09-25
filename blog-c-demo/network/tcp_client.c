#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(int argc, char const *argv[])
{
    int sock;
    struct sockaddr_in my_addr;
    int len;
    char buf[100];
    char recbuf[100];

    if (argc < 3)
    {
        printf("Usage: %s <ip> <port>\n", argv[0]);
        exit(1);
    }

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("socket error");
        exit(1);
    }

    my_addr.sin_family = AF_INET;
    my_addr.sin_port = htons(atoi(argv[2]));
    if (inet_aton(argv[1], (struct in_addr *)&my_addr.sin_addr.s_addr) == 0)
    {
        perror("change error");
        exit(1);
    }

    if (connect(sock, (struct sockaddr *)&my_addr, sizeof(struct sockaddr)) < 0)
    {
        perror("connect error");
        exit(1);
    }
    printf("connected...\n");
    while (1)
    {
        /* code */
        printf("input data to send:");
        fgets(buf, 100, stdin);
        if (strcmp("quit", buf)==0)
        {
            break;
        }

        len = send(sock, buf, strlen(buf) - 1, 0);
        if (len < 0)
        {
            perror("send error");
            exit(1);
        }

        len = recv(sock, recbuf, 100, 0);
        recbuf[len] = '\0';
        if (len < 0)
        {
            perror("recv error");
            exit(1);
        }
        printf("receive data from server: %s\n", recbuf);
    }
    printf("close...\n");
    close(sock);

    return 0;
}
