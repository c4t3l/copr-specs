# Generated from nori-2.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name nori

Name: rubygem-%{gem_name}
Version: 2.6.0
Release: 1%{?dist}
Summary: XML to Hash translator
License: MIT
URL: https://github.com/savonrb/nori
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.2
# BuildRequires: rubygem(nokogiri) >= 1.4.0
# BuildRequires: rubygem(rspec) >= 2.12
# BuildRequires: rubygem(rspec) < 3
BuildArch: noarch

%description
XML to Hash translator.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/benchmark
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/nori.gemspec
%{gem_instdir}/spec

%changelog
* Sun Sep 11 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.6.0-1
- Initial package
