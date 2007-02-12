Summary:	A collection of BSD (Berkeley Standard Distribution) games
Summary(de.UTF-8):	Diverse BSD-Games
Summary(es.UTF-8):	Paquete con varios juegos BSD
Summary(fr.UTF-8):	Paquetage de jeux BSD divers
Summary(pl.UTF-8):	Zestaw gier BSD (Berkeley Standard Distribution)
Summary(pt.UTF-8):	Pacote com vários jogos BSD
Summary(tr.UTF-8):	Metin ekranda oyunlar paketi
Name:		bsd-games
Version:	2.17
Release:	0.2
License:	distributable
Group:		Applications/Games
Source0:	ftp://ibiblio.org/pub/Linux/games/%{name}-%{version}.tar.gz
# Source0-md5:	238a38a3a017ca9b216fc42bde405639
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	5ed0ae6b7c5d5a2edddc636240314e34
Patch0:		%{name}-hole.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-ospeed.patch
Patch3:		%{name}-from.patch
Patch4:		%{name}-monop_rename.patch
Patch5:		%{name}-man.patch
Patch6:		%{name}-types.patch
Patch7:		%{name}-tetris.patch
Patch8:		%{name}-debian.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	groff
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	words
Requires:	textutils
Requires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gamesdir	%{_bindir}
%undefine	with_ccache

%description
Bsd-games includes adventure, arithmetic, atc, backgammon, battlestar,
bcd, caesar, canfield, cfscores, countmail, cribbage, dm, factor,
fish, gomoku, hunt, mille, monop, morse, number, phantasia, pig, pom,
ppt, primes, quiz, rain, random, robots, rot13, sail, snake, snscore,
teachgammon, tetris-bsd, trek, wargames, worm, worms and wump.

Note: countmail requires frm(1) command from elm package.

%description -l de.UTF-8
Dies ist eine Sammlung von Games. Zu den bekanntesten gehören
Backgammon, Cribbage, Monop, Primes, Trek und Battlestar.

%description -l es.UTF-8
Bsd-games incluye juegos: adventure, arithmetic, atc, backgammon,
battlestar, bcd, caesar, canfield, cfscores, countmail, cribbage, dm,
factor, fish, gomoku, hunt, mille, monop, morse, number, phantasia,
pig, pom, ppt, primes, quiz, rain, random, robots, rot13, sail, snake,
snscore, teachgammon, tetris-bsd, trek, wargames, worm, worms and
wump.

Aviso: countmail requiere comando frm(1) del paquete elm.

%description -l fr.UTF-8
Lot de jeux. Contient backgammon, cribbage, le pendu, monop, primes,
trek et battlestar.

%description -l pl.UTF-8
W skład gier BSD wchodzą: adventure, arithmetic, atc, backgammon,
battlestar, bcd, caesar, canfield, cfscores, countmail, cribbage, dm,
factor, fish, gomoku, hunt, mille, monop, morse, number, phantasia,
pig, pom, ppt, primes, quiz, rain, random, robots, rot13, sail, snake,
snscore, teachgammon, tetris-bsd, trek, wargames, worm, worms i wump.

Uwaga: countmail wymaga polecenia frm(1) z pakietu elm.

%description -l pt.UTF-8
Isto é um conjunto de jogos. Os destaques incluem gamão, jogo de
cartas, forca, monopólio e guerra nas estrelas.

%description -l tr.UTF-8
Tavla, cribbage, adam asmaca, monop, primes, trek ve battlestar gibi
oyunlar içeren bir paket.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

cat >config.params <<EOF
bsd_games_cfg_non_interactive=y
bsd_games_cfg_install_prefix=$RPM_BUILD_ROOT
bsd_games_cfg_no_build_dirs="banner factor fortune hack"
bsd_games_cfg_gamesdir=%{_bindir}
bsd_games_cfg_sbindir=%{_sbindir}
bsd_games_cfg_docdir=%{_docdir}/bsdgames-%{version}
bsd_games_cfg_do_chown=n
bsd_games_cfg_gzip_manpages=n
bsd_games_cfg_ncurses_includes=-I/usr/include/ncurses
bsd_games_cfg_ncurses_lib="-lncurses -ltinfo"
EOF

%build
./configure
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	LDFLAGS="%{rpmldflags}" \
	OPTIMIZE="%{rpmcflags}"

mkdir -p doc/trek
nroff trek/DOC/read_me.nr > doc/trek/read_me.txt
nroff trek/DOC/trekmanual.nr > doc/trek/trekmanual.txt

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

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

rm -f $RPM_BUILD_ROOT%{_mandir}/{README.bsd-games-non-english-man-pages,bsd-games-pld.patch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/trek trek/USD.doc/trek.me
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/huntd
%{_datadir}/games/*
%{_datadir}/misc/acronyms
%{_datadir}/misc/acronyms.comp
/var/games/atc_score
/var/games/battlestar.log
/var/games/cfscores
/var/games/criblog
/var/games/robots_roll
%dir /var/games/phantasia
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
