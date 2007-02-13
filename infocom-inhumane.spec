%define		_name		inhumane
Summary:	Infocom text game - Inhumane
Summary(pl.UTF-8):	Tekstówka Infocomu - Inhumane
Name:		infocom-inhumane
Version:	31415926
Release:	2
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z5
# Source0-md5:	84d3ce7ccfafb873736490811a0cc78c
URL:		http://www.ifarchive.org/
Requires:	zcode-wrapper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
A parody of Infocom's Infidel, written when the author was fifteen,
then converted to Inform. To collect a treasure, you must show an
ancient guardian how awful an adventurer you are.

%description -l pl.UTF-8
Parodia Infidela Infocomu napisana gdy autor miał piętnaście lat,
która następnie została przerobiona aby korzystać z Informu. Aby
zgromadzić skarb trzeba wykazać antycznemu strażnikowi jakim się jest
okropnym poszukiwaczem przygód.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/zcode}

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z5
