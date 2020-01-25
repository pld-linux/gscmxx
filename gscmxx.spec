Summary:	Gtk-frontend for scmxx
Summary(pl.UTF-8):	Graficzna nakładka na program scmxx korzystająca z perl-GTK
Name:		gscmxx
Version:	0.4.1
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gscmxx/%{name}-%{version}.tar.gz
# Source0-md5:	5efea1ca76d0e32928e9decde8525f14
Patch0:		%{name}-DESTDIR.patch
URL:		http://gscmxx.sourceforge.net/
BuildRequires:	perl-gtk
BuildRequires:	perl-Image-Size
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	scmxx > 0.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk-frontend for scmxx.

%description -l pl.UTF-8
Graficzna nakładka na program scmxx korzystająca z perl-GTK.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL \
	PREFIX=%{_prefix} \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README doc/Features.txt TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/i18n
%{_datadir}/%{name}/i18n/english
%lang(de) %{_datadir}/%{name}/i18n/german
%lang(it) %{_datadir}/%{name}/i18n/italian
%lang(hu) %{_datadir}/%{name}/i18n/magyar
%{perl_vendorlib}/SCMxx*
%{_mandir}/man1/*
%{_mandir}/man3/SCMxx*
