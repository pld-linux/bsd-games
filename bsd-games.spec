Summary:	A collection of BSD (Berkeley Standard Distribution) games.
Summary(pl):	Zestaw gier BSD (Berkeley Standard Distribution).
Name:		bsd-games
Version:	2.10
Release:	1
Copyright:	distributable
Group:		Games
Group(pl):	Gry
Source0:	ftp://metalab.unc.edu/pub/Linux/games/%{name}-%{version}.tar.gz
Patch0:		%{name}-hole.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-from.patch
Patch3:		%{name}-ospeed.patch
Patch4:		%{name}-config.patch
BuildRequires:	ncurses-devel >= 5.0
Requires:	ncurses >= 5.0
Requires:	textutils 
Requires:	/usr/bin/frm
Buildroot:	/tmp/%{name}-%{version}-root

%description
Bsd-games includes adventure, arithmetic, atc, backgammon, battlestar, bcd,
caesar, canfield, cfscores, countmail, cribbage, dm, factor, fish, gomoku,
hunt, mille, monop, morse, number, phantasia, pig, pom, ppt, primes, quiz,
rain, random, robots, rot13, sail, snake, snscore, teachgammon, tetris-bsd,
trek, wargames, worm, worms and wump.

%description -l pl
W sk³ad gier BSD wchodz±: adventure, arithmetic, atc, backgammon,
battlestar, bcd, caesar, canfield, cfscores, countmail, cribbage, dm,
factor, fish, gomoku, hunt, mille, monop, morse, number, phantasia, pig,
pom, ppt, primes, quiz, rain, random, robots, rot13, sail, snake, snscore,
teachgammon, tetris-bsd, trek, wargames, worm, worms i wump

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
chmod +x install-man install-score
make INSTALL_PREFIX="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/games/*
/usr/share/games/*
/usr/share/misc/acronyms
/var/games/atc_score
/var/games/battlestar.log
/var/games/cfscores
/var/games/criblog
/var/games/robots_roll
%attr(640,root,root) /var/games/phantasia/characs
/var/games/phantasia/gold
/var/games/phantasia/lastdead
/var/games/phantasia/mess
/var/games/phantasia/monsters
/var/games/phantasia/motd
/var/games/phantasia/scoreboard
/var/games/phantasia/void
%attr(750,root,root) /var/games/sail/
/var/games/saillog
/var/games/snake.log
/var/games/snakerawscores
/var/games/tetris-bsd.scores
%{_mandir}/man*/*
