Summary:	A collection of BSD (Berkeley Standard Distribution) games
Summary(de):	Diverse BSD-Games
Summary(es):	Paquete con varios juegos BSD
Summary(fr):	Paquetage de jeux BSD divers
Summary(pl):	Zestaw gier BSD (Berkeley Standard Distribution)
Summary(pt):	Pacote com vários jogos BSD
Summary(tr):	Metin ekranda oyunlar paketi
Name:		bsd-games
Version:	2.14
Release:	2
License:	distributable
Group:		Applications/Games
Source0:	ftp://ibiblio.org/pub/Linux/games/%{name}-%{version}.tar.gz
# Source0-md5:	29042cbe4a71038f84125d020ba28546
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	53f612734e8324dfc7d3658c33dee4cb
Patch0:		%{name}-hole.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-ospeed.patch
Patch3:		%{name}-config.patch
Patch4:		%{name}-from.patch
BuildRequires:	bison
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	words
Requires:	textutils
Requires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gamesdir	%{_bindir}

%description
Bsd-games includes adventure, arithmetic, atc, backgammon, battlestar,
bcd, caesar, canfield, cfscores, countmail, cribbage, dm, factor,
fish, gomoku, hunt, mille, monop, morse, number, phantasia, pig, pom,
ppt, primes, quiz, rain, random, robots, rot13, sail, snake, snscore,
teachgammon, tetris-bsd, trek, wargames, worm, worms and wump.

Note: countmail requires frm(1) command from elm package.

%description -l de
Dies ist eine Sammlung von Games. Zu den bekanntesten gehören
Backgammon, Cribbage, Monop, Primes, Trek und Battlestar.

%description -l es
Esto es un conjunto de juegos. Los destaques incluyen gammon, barajas,
ahorcado, monopolio y guerra en las estrellas.

%description -l fr
Lot de jeux. Contient backgammon, cribbage, le pendu, monop, primes,
trek et battlestar.

%description -l pl
W sk³ad gier BSD wchodz±: adventure, arithmetic, atc, backgammon,
battlestar, bcd, caesar, canfield, cfscores, countmail, cribbage, dm,
factor, fish, gomoku, hunt, mille, monop, morse, number, phantasia,
pig, pom, ppt, primes, quiz, rain, random, robots, rot13, sail, snake,
snscore, teachgammon, tetris-bsd, trek, wargames, worm, worms i wump.

Uwaga: countmail wymaga polecenia frm(1) z pakietu elm.

%description -l pt
Isto é um conjunto de jogos. Os destaques incluem gamão, jogo de
cartas, forca, monopólio e guerra nas estrelas.

%description -l tr
Tavla, cribbage, adam asmaca, monop, primes, trek ve battlestar gibi
oyunlar içeren bir paket.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# config patch creation: diff between unconfigured and following configuration:
# Install prefix: $INSTALL_PREFIX
# Games not to build: banner factor fortune hack
# Games directory: /usr/bin
# Daemon directory: /usr/sbin
# Set owners/groups on installed files [y]: n
# Gzip manpages [y]: n
# Ncurses includes []: -I/usr/include/ncurses
# (the rest is default)

%build
%{__make} \
	LDFLAGS="%{rpmldflags}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
chmod +x install-man install-score

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# primes(6) man originally is just a symlink to factor(6)
# but we install only primes, not factor (which is in sh-utils)
rm -f $RPM_BUILD_ROOT%{_mandir}/man6/primes.6*
install factor/factor.6 $RPM_BUILD_ROOT%{_mandir}/man6/primes.6

# TODO: add Finish factor.6 to non-english-man-pages
#mv -f $RPM_BUILD_ROOT%{_mandir}/fi/man6/{factor,primes}.6

# resolve conflict with hunt package
mv -f $RPM_BUILD_ROOT%{_bindir}/hunt{,-game}
mv -f $RPM_BUILD_ROOT%{_mandir}/man6/hunt{,-game}.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/*
%{_datadir}/misc/acronyms
/var/games/atc_score
/var/games/battlestar.log
/var/games/cfscores
/var/games/criblog
/var/games/robots_roll
%attr(640,root,games) /var/games/phantasia/characs
/var/games/phantasia/gold
/var/games/phantasia/lastdead
/var/games/phantasia/mess
/var/games/phantasia/monsters
/var/games/phantasia/motd
/var/games/phantasia/scoreboard
/var/games/phantasia/void
%attr(750,root,games) /var/games/sail
/var/games/saillog
/var/games/snake.log
/var/games/snakerawscores
/var/games/tetris-bsd.scores
%{_mandir}/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(pl) %{_mandir}/pl/man*/*
