Last login: Mon Sep  1 16:55:09 on ttys008
~ ❯ ssh ubuntu@10.150.2.10                                          05:27:57 AM
(ubuntu@10.150.2.10) Password:
Welcome to Ubuntu 24.04.3 LTS (GNU/Linux 6.8.0-1031-raspi aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Sep  1 17:28:13 KST 2025

  System load:  0.03              Temperature:            57.0 C
  Usage of /:   4.1% of 56.78GB   Processes:              149
  Memory usage: 6%                Users logged in:        1
  Swap usage:   0%                IPv4 address for wlan0: 10.150.2.10


Expanded Security Maintenance for Applications is not enabled.

3 updates can be applied immediately.
3 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Mon Sep  1 17:14:52 2025 from 10.150.2.121
ubuntu@ubuntu:~$ sudo apt-install python
sudo: apt-install: command not found
ubuntu@ubuntu:~$ sudo apt install python
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Package python is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
However the following packages replace it:
  2to3 python-is-python3

E: Package 'python' has no installation candidate
ubuntu@ubuntu:~$ pwd
/home/ubuntu
ubuntu@ubuntu:~$ ls
workspace  workspaceE
ubuntu@ubuntu:~$ cd workspaceE
ubuntu@ubuntu:~/workspaceE$ ls
README.md  system_info.py  test.txt
ubuntu@ubuntu:~/workspaceE$ sudo apt install python
Reading package lists... Done
Building dependency tree... Done
  GNU nano 7.2                       New Buffer *
        up_pos(key)
        print("정답입니다!")
    else:
        down_pos(key)
        print(f'틀렸습니다.정답은 " {answer} " 입니다.')
    print("\n\n\n")
    print("-------------------------------------------------------------------->

file = input("단어장 이름을 작성하시오: ")
try:
    with open(f"{file}.txt", 'r', encoding='utf-8') as file:
        for line in file:
            # 줄바꿈 문자 제거 및 '/'로 분리
            parts = line.strip().split('/')

            # 정확히 두 부분으로 나뉘었는지 확인
            if len(parts) == 2:
                english_word = parts[0].strip()
                meaning = parts[1].strip()
                word_dict[english_word] = meaning
                first.append(english_word)

^G Help      ^O Write Out ^W Where Is  ^K Cut       ^T Execute   ^C Location
^X Exit      ^R Read File ^\ Replace   ^U Paste     ^J Justify   ^/ Go To Line
