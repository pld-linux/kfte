Summary:	KDE FTE - A syntax highlighting programmer editor
Summary(fr.UTF-8):	KDE FTE - Un editeur avec colorisation de la syntaxe
Summary(pl.UTF-8):	KDE FTE - edytor programisty z podświetlaniem składni
Name:		kfte
Version:	0.7.1
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/kfte/%{name}-%{version}.tar.bz2
# Source0-md5:	7a31f799bfb4eefcdf37f639b1965b4b
URL:		http://sourceforge.net/projects/kfte/
BuildRequires:	fam-devel
BuildRequires:	gpm-devel
BuildRequires:	kdelibs-devel >= 9:3.1
BuildRequires:	libart_lgpl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE FTE - A syntax highlighting programmer editor.

%description -l fr.UTF-8
KDE FTE - Un editeur avec colorisation de la syntaxe.

%description -l pl.UTF-8
KDE FTE - edytor programisty z podświetlaniem składni.

%prep
%setup -q

%build
%configure
%{__make} \
	vfte_LDADD="-lgpm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kfte.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{BUGS,HISTORY,README*}
%attr(755,root,root) %{_bindir}/kfte
# other FTE versions - here? there is no other *FTE package
%attr(755,root,root) %{_bindir}/[cqvx]fte
%{_desktopdir}/kde/kfte.desktop
%{_datadir}/apps/kfte
