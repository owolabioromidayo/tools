#include <stdio.h>
#include <string.h>
#include <sys/utsname.h>

int main(void)
{
    struct utsname buf;
    memset(&buf, 0, sizeof buf);

    int ret = uname(&buf);
    if (ret == 0)
    {
        if (strstr(buf.release, "Microsoft"))
            printf("WSL1\n");
        else
            printf("WSL2\n");
    }
    else
        printf("uname error\n");

}