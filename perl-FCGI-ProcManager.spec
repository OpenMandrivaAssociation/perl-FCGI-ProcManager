%define upstream_name	 FCGI-ProcManager
Name:		perl-%{upstream_name}
Version:	0.28
Release:	2

Summary:	Functions for managing FastCGI applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.shadowcat.co.uk/catagits/FCGI-ProcManager
Source0:	https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/FCGI-ProcManager-0.28.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
FCGI::ProcManager is used to serve as a FastCGI process manager. By
re-implementing it in perl, developers can more finely tune performance in
their web applications, and can take advantage of copy-on-write semantics
prevalent in UNIX kernel process management.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/FCGI
%{_mandir}/*/*

%changelog
* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 399601
- update to 0.19
- using %0.28 fixed license & source fields

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.18-3mdv2009.0
+ Revision: 256865
- rebuild

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
+ Revision: 135968
- update to new version 0.18

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-2mdv2008.0
+ Revision: 86379
- rebuild


* Wed Jun 07 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.17-1mdv2007.0
- Initial Mandriva release.


