%define upstream_name	 FCGI-ProcManager
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Functions for managing FastCGI applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/FCGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
FCGI::ProcManager is used to serve as a FastCGI process manager. By
re-implementing it in perl, developers can more finely tune performance in
their web applications, and can take advantage of copy-on-write semantics
prevalent in UNIX kernel process management.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

