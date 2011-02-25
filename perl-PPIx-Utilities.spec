#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	PPIx
%define		pnam	Utilities
%include	/usr/lib/rpm/macros.perl
Summary:	PPIx::Utilities - extensions to PPI
Summary(pl.UTF-8):	PPIx::Utilities - rozszerzenia do PPI
Name:		perl-PPIx-Utilities
Version:	1.001000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/EL/ELLIOTJS/PPIx-Utilities-%{version}.tar.gz
# Source0-md5:	4dc113960205173cf114ae3bdaa37f61
URL:		http://search.cpan.org/dist/PPIx-Utilities/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-PPI >= 1.208
BuildRequires:	perl-Readonly
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-Deep
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of functions for dealing with PPI objects, many
of which originated in Perl::Critic. They are organized into modules
by the kind of PPI class they relate to, by replacing the "PPI" at the
front of the module name with "PPIx::Utilities", e.g. functionality
related to PPI::Nodes is in PPIx::Utilities::Node.

%description -l pl.UTF-8
Ten pakiet to zestaw funkcji operujących na obiektach PPI, z których
wiele pochodzi z modułu Perl::Critic. Funkcje są zorganizowane w
moduły według klas PPI, do których się odnoszą, z początkiem "PPI"
zastąpionym przez "PPIx::Utilities", np. funkcje związane z PPI::Nodes
znajdują się w PPIx::Utilities::Node.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PPIx/Utilities.pm
%{perl_vendorlib}/PPIx/Utilities
%{_mandir}/man3/PPIx::Utilities*.3pm*
