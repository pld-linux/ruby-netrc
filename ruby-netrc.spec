#
# Conditional build:
%bcond_without	tests		# build without tests

%define	gem_name netrc
Summary:	Library to read and write netrc files
Name:		ruby-%{gem_name}
Version:	0.7.7
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	1322b2053484eec64992e00c7f71cd69
URL:		https://github.com/geemus/netrc
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	rubygem-minitest
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
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
testrb -Ilib test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md LICENSE changelog.txt
%{ruby_vendorlibdir}/netrc.rb
