%define upstream_name    Directory-Scratch-Structured
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Creates temporary files and directories from a structured description
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Directory/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::TreeDumper)
BuildRequires:	perl(Directory::Scratch)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::Block)
BuildRequires:	perl(Test::Dependencies)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Spelling)
BuildRequires:	perl(Test::Strict)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This module adds a _create_structured_tree_ subroutine to the the
Directory::Scratch manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%check
rm -f t/003_perl_critic.t
./Build test

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Directory


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 681426
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 403153
- rebuild using %%perl_convert_version

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 320428
- update to new version 0.04

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 268447
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
+ Revision: 214055
- drop optional Test::Distribution dependency
- import perl-Directory-Scratch-Structured


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
- first mdv release
