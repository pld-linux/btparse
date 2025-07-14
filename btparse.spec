# NOTE: for versions >= 0.36 see perl-Text-BibTeX.spec
#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	C library to parse BibTeX files
Summary(pl.UTF-8):	Biblioteka C do analizy plików BibTeXa
Name:		btparse
Version:	0.34
Release:	1.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.gerg.ca/software/btOOL/%{name}-%{version}.tar.gz
# Source0-md5:	87d09ce6331c57cc2da30b5c83f545e0
Patch0:		%{name}-format.patch
URL:		http://www.gerg.ca/software/btOOL/
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
btparse is the C component of btOOL, a pair of libraries for parsing
and processing BibTeX files. Its primary use is as the back-end to
Text::BibTeX library for Perl (the other half of btOOL), but there's
nothing to prevent you from writing C programs using btparse - or from
writing extensions to other high-level languages using btparse as a
back-end.

%description -l pl.UTF-8
btparse to część C narzędzia btOOL - pary bibliotek do analizy i
przetwarzania plików BibTeX. Głównym zastosowaniem jest backend dla
biblioteki Text::BibTeX dla Perla (drugiej połówki narzędzia btOOL),
ale nic nie stoi na przeszkodzie pisaniu programów w C
wykorzystujących btparse albo rozszerzeń dla innych wysokopoziomowych
języków z wykorzystaniem btparse jako backendu.

%package devel
Summary:	Header files for btparse library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki btparse
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for btparse library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki btparse.

%package static
Summary:	Static btparse library
Summary(pl.UTF-8):	Statyczna biblioteka btparse
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static btparse library.

%description static -l pl.UTF-8
Statyczna biblioteka btparse.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbtparse.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/bibparse
%attr(755,root,root) %{_libdir}/libbtparse.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbtparse.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbtparse.so
%{_includedir}/btparse.h
%{_mandir}/man3/bt_*.3*
%{_mandir}/man3/btparse.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libbtparse.a
%endif
