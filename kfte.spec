Summary:	KDE FTE - A syntax highlighting programmer editor
Summary(fr):	KDE FTE - Un editeur avec colorisation de la syntaxe
Summary(pl):	KDE FTE - edytor programisty z pod¶wietlaniem sk³adni
Name:		kfte
Version:	6.1
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.kde.org/pub/kde/Attic/old/1.1.2/apps/utils/%{name}-V%{version}.tgz
# Source0-md5:	7c0673f36d350d5ca2bc45774d05c8f0
#Patch0:		%{name}-%{version}.patch.bz2
#URL:		http://ixtas.fri.uni-lj.si/~markom/fte/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE FTE - A syntax highlighting programmer editor.

%description -l fr
KDE FTE - Un editeur avec colorisation de la syntaxe.

%description -l pl
KDE FTE - edytor programisty z pod¶wietlaniem sk³adni.

%prep
%setup -q
#%patch -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install
# prefix=$RPM_BUILD_ROOT%{prefix}
tar cf - config | ( cd $RPM_BUILD_ROOT%{_datadir}/apps/%{name} ; tar xf - )
cd $RPM_BUILD_ROOT%{_datadir}/apps/%{name}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel
$RPM_BUILD_ROOT%{_bindir}/cfte config/main.fte $RPM_BUILD_ROOT%{_sysconfdir}/skel/.fterc

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
