Summary: A collection of BSD (Berkeley Standard Distribution) games.
Name: bsd-games
Version: 2.7
Release: 3
Copyright: distributable
Group: Amusements/Games
Source0: ftp://metalab.unc.edu/pub/Linux/games/bsd-games-2.7.tar.gz
Patch0: bsd-games-2.7-config.patch
Patch1: bsd-games-2.7-hole.patch
Patch2: bsd-games.patch
Patch3: bsd-games-from.patch
Buildroot: /var/tmp/bsd-games
Requires: textutils /usr/bin/frm

%description
Bsd-games includes adventure, arithmetic, atc, backgammon, battlestar,
bcd, caesar, canfield, cfscores, countmail, cribbage, dm, factor,
fish, gomoku, hangman, hunt, mille, monop, morse, number, phantasia,
pig, pom, ppt, primes, quiz, rain, random, robots, rot13, sail, snake,
snscore, teachgammon, tetris-bsd, trek, wargames, worm, worms and
wump.

%prep
%setup -q
%patch -p1 -b .config
%patch1 -p1 -b .hole
%patch2 -p1 -b .tim
%patch3 -p1 -b .from
chmod +x install-man
chmod +x install-score

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
make RPM_BUILD_ROOT="$RPM_BUILD_ROOT" install

find $RPM_BUILD_ROOT/usr/games -type f | sed "s|$RPM_BUILD_ROOT||g" |
  sed "s|/usr/games/dm|%attr\(2755,root,games\) /usr/games/dm|" > files.list
 

%clean
rm -rf $RPM_BUILD_ROOT

%files -f files.list
%defattr(-,root,root)
/usr/lib/games/*
/var/lib/games/*
/usr/share/games/*
/usr/man/man5/*
/usr/man/man6/*
/usr/man/man8/*
/usr/sbin/*

%changelog
* Sat Aug 21 1999 Bill Nottingham <notting@redhat.com>
- fix countmail (#3722). I must be bored.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- make dm setgid games, not setuid root...

* Fri Jul 9 1999 Tim Powers <timp@redhat.com>
- updated source to 2.7
- updated patches to fix bugs and the braindead configure script, 
  dropped a few of the older patches that made it into this release
- replaced -make install with make install-strip
- built for 6.1

* Wed May 12 1999 Bill Nottingham <notting@redhat.com>
- pick up some more files

* Thu Apr 01 1999 Michael Maher <mike@redhat.com>
- only a fool would add a dependency to this package on a 
  day like today.

* Fri Mar 18 1999 Michael Maher <mike@redhat.com>
- fixed bug 1550

* Mon Feb 08 1999 Michael Maher <mike@redhat.com>
- moved pacakge to PowerTools.

* Thu Jun 18 1998 Alan Cox <alan@redhat.com>
- Chris Evans pointed out a hole in sail I missed.

* Wed Jun 17 1998 Alan Cox <alan@redhat.com>
- Stopped people using cribbage to be able to cheat game score files.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed the config patch so that it will build on non /usr/src/redhat build
  trees

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to bsd-games 2.1
- started over on package
