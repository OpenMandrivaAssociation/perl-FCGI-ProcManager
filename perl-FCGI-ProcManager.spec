%define module	FCGI-ProcManager
%define name	perl-%{module}
%define version 0.17
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Functions for managing FastCGI applications
License:	GPL or Artistic
Group:		Development/Perl
Source:		%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
FCGI::ProcManager is used to serve as a FastCGI process manager. By
re-implementing it in perl, developers can more finely tune performance in
their web applications, and can take advantage of copy-on-write semantics
prevalent in UNIX kernel process management.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/FCGI
%{_mandir}/*/*

