#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname netrc
Summary:	Library to read and write netrc files
Name:		ruby-%{pkgname}
Version:	0.7.9
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	177ed2c83e6037aed863144a53a39021
URL:		https://github.com/heroku/netrc
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	gnupg
BuildRequires:	ruby-minitest
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library can read and update netrc files, preserving formatting
including comments and whitespace.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -n %{pkgname}-%{version}

chmod 600 data/newlineless.netrc

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
testrb -Ilib test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md LICENSE.md changelog.txt
%{ruby_vendorlibdir}/netrc.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
