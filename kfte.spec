Summary:	KDE FTE - A syntax highlighting programmer editor
Summary(fr):	KDE FTE - Un editeur avec colorisation de la syntaxe
Name:		kfte
Version:	6.1
Release:	1
License:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}-%{version}.patch.bz2
URL:		http://ixtas.fri.uni-lj.si/~markom/fte
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
KDE FTE - A syntax highlighting programmer editor

%description -l fr
KDE FTE - Un editeur avec colorisation de la syntaxe

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch -p0

%build
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS CXXFLAGS
%configure
make

%install
make install
# prefix=$RPM_BUILD_ROOT/%{prefix}
tar cf - config | ( cd $RPM_BUILD_ROOT%{prefix}/share/apps/%{name}/ ; tar xf - )
cd $RPM_BUILD_ROOT%{prefix}/share/apps/%{name}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel
$RPM_BUILD_ROOT%{prefix}/bin/cfte config/main.fte $RPM_BUILD_ROOT%{_sysconfdir}/skel/.fterc

if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]; then
  find $RPM_BUILD_ROOT%{_prefix}/man -type f -exec bzip2 -9f {} \;
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
%defattr(644,root,root,755)
