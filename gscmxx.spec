%include /usr/lib/rpm/macros.perl
Summary(pl):	Graficzna nak³adka na program scmxx korzystaj±ca z perl-GTK
Summary:	Gtk-frontend for scmxx
Name:		gscmxx
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/gscmxx/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gscmxx.sourceforge.net
BuildRequires:	perl-gtk
BuildRequires:	perl-Image-Size
Requires:	scmxx > 0.6.0
Provides:	perl(SCMxx::Config)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README doc/Features.txt TODO
%attr(755,root,root) %{_bindir}/*
/usr/share/pixmaps/%{name}
%{_datadir}/%{name}
%{perl_sitelib}/*
