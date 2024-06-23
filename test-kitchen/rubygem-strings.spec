# Generated from strings-0.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name strings

Name: rubygem-%{gem_name}
Version: 0.2.1
Release: 1%{?dist}
Summary: A set of methods for working with strings
License: MIT
URL: https://github.com/piotrmurach/strings
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
# BuildRequires: rubygem(rspec) >= 3.0
BuildArch: noarch

%description
A set of methods for working with strings such as align, truncate, wrap and
many more.


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
# rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sun Sep 11 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.2.1-1
- Initial package
