%define module   Directory-Scratch-Structured
%define version    0.03
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    creates temporary files and directories from a structured description
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Directory/%{module}-%{version}.tar.gz
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Directory::Scratch)
BuildRequires: perl(Readonly)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Dependencies)
BuildRequires: perl(Test::Distribution)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Spelling)
BuildRequires: perl(Test::Strict)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module adds a _create_structured_tree_ subroutine to the the
Directory::Scratch manpage.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Directory

