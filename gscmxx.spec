%include /usr/lib/rpm/macros.perl
Summary:	Gtk-frontend for scmxx
Summary(pl):	Graficzna nak³adka na program scmxx korzystaj±ca z perl-GTK
Name:		gscmxx
Version:	0.4.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gscmxx/%{name}-%{version}.tar.gz
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

%description -l pl
Graficzna nak³adka na program scmxx korzystaj±ca z perl-GTK.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL \
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
%{_datadir}/%{name}
%{perl_vendorlib}/*
