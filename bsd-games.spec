Summary:	A collection of BSD (Berkeley Standard Distribution) games.
Summary(de):	Diverse BSD-Games  
Summary(fr):	paquetage de jeux BSD divers
Summary(tr):	Metin ekranda oyunlar paketi
Name:		bsd-games
Version:	2.7
Release:	3
Copyright:	distributable
Group:		Amusements/Games
Source0:	ftp://metalab.unc.edu/pub/Linux/games/%{name}-%{version}.tar.gz
Patch0:		bsd-games-2.7-config.patch
Patch1:		bsd-games-2.7-hole.patch
Patch2:		bsd-games.patch
Patch3:		bsd-games-from.patch
Buildroot:	/tmp/%{name}-%{version}-root
Requires:	textutils /usr/bin/frm

%description
Bsd-games includes adventure, arithmetic, atc, backgammon, battlestar,
bcd, caesar, canfield, cfscores, countmail, cribbage, dm, factor,
fish, gomoku, hangman, hunt, mille, monop, morse, number, phantasia,
pig, pom, ppt, primes, quiz, rain, random, robots, rot13, sail, snake,
snscore, teachgammon, tetris-bsd, trek, wargames, worm, worms and
wump.

%description -l de
Dies ist eine Sammlung von Games. Zu den bekanntesten gehören Backgammon,
Cribbage, Monop, Primes, Trek und Battlestar.

%description -l fr
Lot de jeux. Contient backgammon, cribbage, le pendu, monop, primes, trek
et battlestar.

%description -l tr
Tavla, cribbage, adam asmaca, monop, primes, trek ve battlestar gibi oyunlar
içeren bir paket.

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
%defattr(644,root,root,755)
%{_libdir}/games/*
/var/lib/games/*
%{_datadir}/games/*
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_mandir}/man8/*
%{_sbindir}/*
