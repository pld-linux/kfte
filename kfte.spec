%define name kfte
%define version 6.1
%define release 1mdk

Name: %{name}
Summary: KDE FTE - A syntax highlighting programmer editor
Summary(fr): KDE FTE - Un editeur avec colorisation de la syntaxe
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Patch: %{name}-%{version}.patch.bz2
Group: Applications/Editors
URL: http://ixtas.fri.uni-lj.si/~markom/fte
BuildRoot: /tmp/%{name}-buildroot
Copyright: GPL
Packager: Lenny Cartier (lenny@mandrakesoft.com)
Distribution: Mandrake
Prefix: /usr

%description
KDE FTE - A syntax highlighting programmer editor

%description -l fr
KDE FTE - Un editeur avec colorisation de la syntaxe

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{prefix} --with-install-root=$RPM_BUILD_ROOT
make -j 2

%install
make install
# prefix=$RPM_BUILD_ROOT/%{prefix}
tar cf - config | ( cd $RPM_BUILD_ROOT%{prefix}/share/apps/%{name}/ ; tar xf - )
cd $RPM_BUILD_ROOT%{prefix}/share/apps/%{name}
mkdir -p $RPM_BUILD_ROOT/etc/skel
$RPM_BUILD_ROOT%{prefix}/bin/cfte config/main.fte $RPM_BUILD_ROOT/etc/skel/.fterc

if [ -d $RPM_BUILD_ROOT/usr/man ]; then
  find $RPM_BUILD_ROOT/usr/man -type f -exec bzip2 -9f {} \;
fi
if [ -d $RPM_BUILD_ROOT/usr/info ]; then
  find $RPM_BUILD_ROOT/usr/info -type f -exec bzip2 -9f {} \;
fi
if [ -d $RPM_BUILD_ROOT/usr/X11R6/man ]; then
  find $RPM_BUILD_ROOT/usr/X11R6/man -type f -exec bzip2 -9f {} \;
fi
if [ -d $RPM_BUILD_ROOT/usr/lib/perl5/man ]; then
  find $RPM_BUILD_ROOT/usr/lib/perl5/man -type f -exec bzip2 -9f {} \;
fi

cd $RPM_BUILD_ROOT
find . -type d | sed -e '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{name}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
       -e '/\/etc\//s|^|%config|' \
       -e '/\/config\//s|^|%config|' \
       >> $RPM_BUILD_DIR/file.list.%{name}

find . -type l | sed -e 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
%defattr(-,root,root,0755)

%changelog
* Tue Oct 19 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Specfile adaptation for Mandrake

* Fri Aug 06 1999 Stefan Siegel <siegel@informatik.uni-kl.de>
- Added "config" tag for files containing /etc or /config
- Added compression for perl- and localized man-pages

* Sat Jun 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- create (more or less) generic spec file...
