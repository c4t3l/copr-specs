# Generated from unicode_utils-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unicode_utils

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 1%{?dist}
Summary: additional Unicode aware functions for Ruby 1.9
License: BSD-2 Clause
URL: http://github.com/lang/unicode_utils
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.1
BuildArch: noarch

%description
additional Unicode aware functions for Ruby 1.9.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/CHANGES.txt
%{gem_instdir}/INSTALL.txt
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/cdata
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/test

%changelog
* Sun Sep 11 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 1.4.0-1
- Initial package
